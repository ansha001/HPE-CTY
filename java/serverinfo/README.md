## JAVA SETUP

1.Install jdk
```
sudo yum install java-1.8.0-openjdk-devel
```
2.Install Tomcat server package(below version is preferred)
```
wget https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.37/bin/apache-tomcat-8.5.37.tar.gz
```
3.unzip and move package
```
tar -xf apache-tomcat-8.5.37.tar.gz
sudo mv apache-tomcat-8.5.37 /usr/local/tomcat
```
4.Modify bashrc file ( ~/.bashrc ) - Add below commands
```
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
export CATALINA_HOME=/usr/local/tomcat
```
```
source ~/.bashrc
````
5. Running http application
```
/usr/local/tomcat/bin/startup.sh
```
```
cp ../java/serverinfo/src/main/webapp/index.jsp /usr/local/tomcat/webapps/ROOT/index.jsp
```
```
mv ../java/serverinfo/src/main/webapp/server_info.csv /usr/local/tomcat/webapps/ROOT/
```
```
/usr/local/tomcat/bin/startup.sh
```
