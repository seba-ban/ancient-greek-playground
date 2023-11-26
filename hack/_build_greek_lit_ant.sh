# script intended to be run inside a container in `hack/build_greek_lit_ant.sh`

set -e

cd "$(mktemp -d)"

# download ant
# TODO: checksum
curl https://dlcdn.apache.org//ant/binaries/apache-ant-1.10.14-bin.tar.gz -o apache-ant-1.10.14-bin.tar.gz
tar xvf apache-ant-1.10.14-bin.tar.gz
cd apache-ant-1.10.14
export ANT_HOME=$(pwd)
export PATH=${ANT_HOME}/bin:${PATH}

# hack for the build to success
# I don't know which version of java/openjdk should be used to build the project
# so for now all `importClass` statements in .tmp/repos/canonical-greekLit/build.xml
# are replaced with `var` statements, e.g.:
# importClass(java.io.File); -> var File = java.io.File;

cp /data/build.xml /data/build.xml.bak
cp /data/build.xml .
sed -i 's#importClass(\([^;]*\)\.\([^;]*\));#var \2 = \1.\2;#' build.xml
cp build.xml /data/build.xml

# run ant
cd /data
ant

# copy build files
cp build.xml.bak build.xml

# cleanup
rm build.xml.bak
cp build/*.xar /output
rm -rf build