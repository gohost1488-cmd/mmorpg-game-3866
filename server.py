#!/bin/bash
# TrinityCore setup for MMORPG
git clone https://github.com/TrinityCore/TrinityCore.git engine
cd engine
mkdir build && cd build && cmake ../ -DCMAKE_INSTALL_PREFIX=./server && make -j4
echo "Engine ready: TrinityCore"
