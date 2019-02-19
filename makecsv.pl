#!/usr/bin/perl

use strict;

# 35.925606, 136.188622

my $file = "recordfile.csv";

my $name = "ƒgƒ}ƒg"
my $kosu = "";
#my $ido = shift;
#my $kdo = shift;
my $ido = 35.925606;
my $kdo = 136.188622;

open(O, ">$file") || die "open error(w): $file\n";
print(O "$name,$kosu,$ido,$kdo\r\n");
close(O);

exit;
