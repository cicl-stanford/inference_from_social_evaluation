#!/bin/bash
Trees=Trees/*
AgA=A/*
AgB=B/*
AgC=C/*

for trees in $Trees
do
	for A in $AgA
	do
		for B in $AgB
		do
			for C in $AgC
			do
				p1="${trees%%.*}"
				p1="${p1#*/}"
				p1="${p1#*/}"
				p2="_"
				p3="${A%%.*}"
				p3="${p3#*/}"
				p3="${p3#*/}"	
				p4="${B%%.*}"
				p4="${p4#*/}"
				p4="${p4#*/}"
				p5="${C#*/}"
				outputfolder="StimuliOutput/"
				output=$outputfolder$p1$p2$p3$p4$p5
				pdftk "$trees" background "base.pdf" output "temp.pdf"
				pdftk "$A" background "temp.pdf" output "temp2.pdf"
				pdftk "$B" background "temp2.pdf" output "temp.pdf"
				pdftk "$C" background "temp.pdf" output "$output"
			done
		done
	done
done