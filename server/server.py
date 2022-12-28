import asyncio
import json
import re
import time
import uuid
from json import JSONDecodeError
from typing import Optional

from lsprotocol.types import (TEXT_DOCUMENT_COMPLETION, TEXT_DOCUMENT_DID_CHANGE,
                               TEXT_DOCUMENT_DID_CLOSE, TEXT_DOCUMENT_DID_OPEN,
                               TEXT_DOCUMENT_HOVER,
                               TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL,
                               TEXT_DOCUMENT_DEFINITION)
from lsprotocol.types import (CompletionItem, CompletionList, CompletionOptions,
                             CompletionParams, ConfigurationItem,
                             ConfigurationParams, Diagnostic,
                             DidChangeTextDocumentParams,
                             DidCloseTextDocumentParams,
                             DidOpenTextDocumentParams, MessageType, Position,
                             Range, Registration, RegistrationParams,
                             SemanticTokens, SemanticTokensLegend, SemanticTokensParams,
                             Unregistration, UnregistrationParams,
                             WorkDoneProgressBegin, WorkDoneProgressEnd,
                             WorkDoneProgressReport,
                             Hover,HoverOptions,
                             Definition, DefinitionOptions,DefinitionParams,
                             Range, Location, LocationLink
)
from pygls.server import LanguageServer

class ttcn3LanguageServer(LanguageServer):
    CMD_RESTART_SERVER = 'restart_server'
    CONFIGURATION_SECTION = 'ttcn3Server'

    def __init__(self, *args):
        super().__init__(*args)


# Init server
json_server = ttcn3LanguageServer('ccls-for-ttcn3', 'v2.0')




@json_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(server: ttcn3LanguageServer, params: DidChangeTextDocumentParams):
    """Text document did change notification."""
    server.show_message('document changed!')


@json_server.feature(TEXT_DOCUMENT_DEFINITION,DefinitionOptions())
def jonas2(server: ttcn3LanguageServer, params: DefinitionParams):
            # use params.text_document and params.position to figure out where to send client
            location = Location(uri="test.ttcn",
                                range=Range(start=Position(line=0, character=0),end=Position(line=1, character=1),),)
            return location

@json_server.feature(TEXT_DOCUMENT_HOVER,HoverOptions())
def jonas(server: ttcn3LanguageServer, params):
    server.show_message('jonas')
    return Hover("hej")


@json_server.feature(TEXT_DOCUMENT_DID_CLOSE)
def did_close(server: ttcn3LanguageServer, params: DidCloseTextDocumentParams):
    """Text document did close notification."""
    server.show_message('Text Document Did Close')


@json_server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message('Text Document Did Open')


@json_server.command(ttcn3LanguageServer.CMD_RESTART_SERVER)
def restart_server(ls: ttcn3LanguageServer, *args):
    ls.show_message('beep bop bop')
