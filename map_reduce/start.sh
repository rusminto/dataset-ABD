/opt/hadoop/bin/hadoop com.sun.tools.javac.Main ${1}.java
jar cf wc.jar ${1}*.class

rm -r output
/opt/hadoop/bin/hadoop jar wc.jar ${1} input output
