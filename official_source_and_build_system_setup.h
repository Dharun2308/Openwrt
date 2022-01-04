#!/bin/bash

# Install all dependencies
sudo apt update -y

sudo apt install -y build-essential ccache ecj fastjar file g++ gawk \
gettext git java-propose-classpath libelf-dev libncurses5-dev \
libncursesw5-dev libssl-dev python python2.7-dev python3 unzip wget \
python3-distutils python3-setuptools rsync subversion swig time \
xsltproc zlib1g-dev

sudo apt install -y quilt qemu qemu-utils qemu-kvm virt-manager libvirt-daemon-system libvirt-clients bridge-utils busybox curl rsync build-essential asciidoc binutils bzip2 gawk gettext git libncurses5-dev libz-dev patch unzip zlib1g-dev lib32gcc1 libc6-dev-i386 subversion flex uglifyjs git-core gcc-multilib p7zip p7zip-full msmtp libssl-dev texinfo libglib2.0-dev xmlto qemu-utils upx libelf-dev autoconf automake libtool autopoint device-tree-compiler wget
 
sudo apt-get -y install gcc-multilib g++-multilib 

sudo apt update -y

sudo apt upgrade -y

# Clone the source code

git clone https://git.openwrt.org/openwrt/openwrt.git

cd openwrt

git checkout v21.02.1

echo "src-git openmptcprouter https://github.com/Ysurac/openmptcprouter-feeds.git" >>feeds.conf.default

./scripts/feeds clean

./scripts/feeds update -a

./scripts/feeds install -a

# Download the config file and replace existing config file

sudo rm .config
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1l0PvxGo07vF7VlfjIKpg1CBbblb61GDU' -O .config


# Apply MPTCP kernel patches Only for bcm27xx target

# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/690-mptcp_trunk.patch' -o target/linux/bcm27xx/patches-5.4/690-mptcp_trunk.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/692-tcp_nanqinlang.patch' -o target/linux/bcm27xx/patches-5.4/692-tcp_nanqinlang.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/693-tcp_bbr2.patch' -o target/linux/bcm27xx/patches-5.4/693-tcp_bbr2.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/998-ndpi-netfilter.patch' -o target/linux/bcm27xx/patches-5.4/998-ndpi-netfilter.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/999-stop-promiscuous-info.patch' -o target/linux/bcm27xx/patches-5.4/999-stop-promiscuous-info.patch

#curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/690-mptcp_trunk.patch' -o target/linux/generic/hack-5.4/690-mptcp_trunk.patch

curl 'https://raw.githubusercontent.com/arinc9/openwrt/openwrt-21.02-mptcpv0/target/linux/generic/hack-5.4/690-mptcp_v0.96.patch' -o target/linux/generic/hack-5.4/690-mptcp_v0.96.patch
# Apply MPTCP kernel patches Only for x86 target

# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/690-mptcp_trunk.patch' -o target/linux/x86/patches-5.4/690-mptcp_trunk.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/692-tcp_nanqinlang.patch' -o target/linux/x86/patches-5.4/692-tcp_nanqinlang.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/693-tcp_bbr2.patch' -o target/linux/x86/patches-5.4/693-tcp_bbr2.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/998-ndpi-netfilter.patch' -o target/linux/x86/patches-5.4/998-ndpi-netfilter.patch && \
# curl 'https://raw.githubusercontent.com/Ysurac/openmptcprouter/develop/root/target/linux/generic/hack-5.4/999-stop-promiscuous-info.patch' -o target/linux/x86/patches-5.4/999-stop-promiscuous-info.patch

# Test the patches to see if they're applied fine 

make menuconfig -j$(nproc)

make target/linux/{clean,prepare} V=s

make kernel_menuconfig -j$(nproc)

# Finally make the image

make -j$(nproc)




