To generate antlr4:
```
cd /usr/local/lib
sudo wget http://www.antlr.org/download/antlr-4.11.1-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.9.3-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.11.1-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
antlr4 -visitor -Dlanguage=Python3 ttcn3.g4 -o antlr4_files # generate python code
antlr4 -visitor ttcn3.g4 -o java #generate java code
javac *.java # compile java code
Test:
grun ttcn3 ttcn3module test.ttcn -gui
```

