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

clear

# Clone the source code

git clone https://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@github.com/dharun2308/openwrt.git

clear

mv openwrt/openwrt* ./ || echo Error deleting unwanted files!! Will not work as intended..

sudo rm -r openwrt || echo Error deleting unwanted files!! Will not work as intended..

cd openwrt*

./scripts/feeds clean

./scripts/feeds update -a

./scripts/feeds install -a

clear

make menuconfig -j$(nproc)

clear

# Test the patches to see if they're applied fine

make target/linux/{clean,prepare} V=s

clear 

make -j $(($(nproc)+1)) kernel_menuconfig

# Finally make the image

make download

make -j $(($(nproc)+1)) || clear && echo Error building image

clear





