#!/usr/bin/perl

use strict;

my $file = shift;
my $name = shift;
my $kosu = shift;
my $ido = shift;
my $kdo = shift;

open(O, ">$file") || die "open error(w): $file\n";
print(O "$name,$kosu,$ido,$kdo\r\n");
close(O);

exit;
