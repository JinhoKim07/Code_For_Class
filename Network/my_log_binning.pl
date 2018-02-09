#!/usr/bin/perl

use strict;
use warnings;

my $input = $ARGV[0];
open my $fh,"<",$input;

my $logstep = $ARGV[1];

my $basenumber = 2;

my @rawdata;
my %data;

while (<$fh>) {
	chomp;
	my ($number, $value) = split/\t/;
	push (@rawdata, $value);
}

close $fh;
my $logbin;
my $cnt = 0;
for (0..$#rawdata) {

	my $pre_logbin = int(log($rawdata[$_])/log($basenumber) * $logstep)/$logstep;
   
	if ($pre_logbin >= 0) {
		$logbin = $pre_logbin + 1/(2*$logstep);
	}
	else {
		$logbin = $pre_logbin - 1/(2*$logstep);
	}

	if (exists $data{$logbin}) {
		$data{$logbin} ++;
	}
	else {
		$data{$logbin} = 1;
	}
	$cnt ++;

	
#	print "$rawdata[$_]\n$logbin\n";
}

for my $x (sort{$a<=>$b} keys %data) {
	my $prob = $data{$x} / $cnt;
	print "$x\t$prob\t$data{$x}\n";
}

