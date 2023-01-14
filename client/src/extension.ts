"use strict";

import * as net from "net";
import * as path from "path";
import { ExtensionContext, ExtensionMode, workspace,commands, window, StatusBarAlignment } from "vscode";
import {
    LanguageClient,
    LanguageClientOptions,
    ServerOptions,
} from "vscode-languageclient/node";

let client: LanguageClient;

function getClientOptions(): LanguageClientOptions {
    return {
        documentSelector: [
            { scheme: "file", language: "ttcn" },
            { scheme: "untitled", language: "ttcn" },
        ],
        outputChannelName: "ttls",
        synchronize: {
            // Notify the server about file changes to '.clientrc files contain in the workspace
            fileEvents: workspace.createFileSystemWatcher("**/.clientrc"),
        },
    };
}

function startLangServer(
    command: string,
    args: string[],
    cwd: string
): LanguageClient {
    const serverOptions: ServerOptions = {
        args,
        command,
        options: { cwd },
    };

    return new LanguageClient(command, serverOptions, getClientOptions());
}

function createStatusBarItem(context: ExtensionContext)
{
    const myCommandId = 'start_server';
    const item = window.createStatusBarItem(StatusBarAlignment.Left);
    item.command = myCommandId;
    context.subscriptions.push(item);
    item.text = `$(call-outgoing) ttls`;
    item.tooltip = `Click to start indexing`;
    item.show();
}

export function activate(context: ExtensionContext): void {
        // Python 3.8 is required by pygls
        const python_interpreter = workspace.getConfiguration("ttls").get<string>("python_interpreter");
        // wd is where the extension is located
        const wd = workspace.getConfiguration("ttls").get<string>("wd");
        client = startLangServer(python_interpreter, ["-m", "server"], wd);
        createStatusBarItem(context) ;
        context.subscriptions.push(client.start());
}

export function deactivate(): Thenable<void> {
    return client ? client.stop() : Promise.resolve();
}
