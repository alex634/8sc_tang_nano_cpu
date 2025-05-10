# 8sc

## Introduction

This is an 8 bit single cycle CPU implemented on a [Tang Nano 20k](https://wiki.sipeed.com/hardware/en/tang/tang-nano-20k/nano-20k.html). It is inspired by the 32 bit RISC single cycle processor architecture that is used to teach hardware architecture. To reduce complexity in implementation, the least amount of instructions deemed feasible was implemented. This CPU has 8 different instructions, 256 bytes of instruction ROM and 256 bytes of read write data memory.

## Motivation

I had always wanted to design a CPU but I usually would give up before I had any substantial design because I was overwhelmed by the process and was lacking necessary knowledge. I had some free time before finals and had finished courses relevant to designing a CPU. I had taken EECS 443 at KU (Digital Systems Design) this semester and EECS 645 (Hardware Architecture) in an earlier semester. Digital Systems Design taught me how to use hardware description languages to describe a digital circuit and EECS 645 taught me how a basic CPU worked. Since I am going to have to be working soon, I thought that there would be no better time to work on this than now.

## How to use this

The Tang Nano 20k is programmed using the [GOWIN EDA software](https://www.gowinsemi.com/en/support/home/). Specifically, I am using the Education edition (because it is free). To use this project, import it into GOWIN, synthesize it, then do plan and routing. Finally, to write the bitstream to the FPGA, I would suggest using [openFPGAloader](https://github.com/trabucayre/openFPGALoader) if you are on Linux. The GOWIN tool for writing the bitstream doesn't seem to work for some reason on Linux.

If you want to write your own custom programs for this CPU, please check the `Documentation` folder. It has guides on how to write, assemble, and load code. If you write a custom program, you must synthesize, plan and route, and write the bitstream again.
