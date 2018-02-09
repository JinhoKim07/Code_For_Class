#!/usr/bin/perl

use strict;
use warnings;

my $input = $ARGV[0];
open my $fh,"<",$input;

my $step = $ARGV[1];

my @rawdata;
my %data;

while (<$fh>) {

	chomp;
	my ($number, $value) = split/\t/;
#	print "$_\t$value\n";
	push (@rawdata, $value);
}

close $fh;

my $cnt=0;
for (0..$#rawdata) {
	
	my $linear = int($rawdata[$_] * $step)/$step + 1/(2*$step);
#	print "$rawdata[$_]\t$linear\n";
	if (exists $data{$linear}){
		$data{$linear} ++;
	}
	else {
		$data{$linear} = 1;
	}
	$cnt++;

}

for my $x (sort { $a <=> $b } keys %data) {
	my $prob = $data{$x} / $cnt;
	print "$x\t$prob\t$data{$x}\n";
}

