
# Meeting 0 
date: 28-10-2026

# Attendance
All


# Objectives
- Discuss details of the options
	- Implementation 
	- Report (overleaf?/~~github~~)
- how to split work up?
- Set initial deadlines 
	-  implemenation sections
	- job submitted
	- report complete
- Schedule future meetings (2/week w8-11 )
- Organisation strategy (github project/issues, whatsapp, meetings?)
- Github repo join 
- Code Styling (linters, tests, ci, PRs)
	- whats necessary/benificial and what's not 


# Decisions Made
- Project B 


## Tasks and workload split
10.2 - 1 person (Tom) 

- fft_serial.c, complete the FFT call in run_example
- Add the two one-dimensional FFT outputs
- and a comparison with the expected values above

10.3 - 1 person (Maks)
- Complete the MPI_Scatter call to give each rank mN complex values
- Complete the distributed transpose
	1.
	2.
	3
- real double, so use MPI_DOUBLE
 
10.3 - 1 person (Sam)
- diagram of the two ranks’ send and receive buffers for  the worked transpose
- MPI code sections and the results of the
- why transposing a matrix whose ranks own consesutive rows requires communication such as MPI_Alltoall


10.4 - 1 person  (Chester)
- Complete its MPI_Allreduce call to report the largest elapsed time across ranks
- plot of median runtime against process count, and a speedup plot
- explanation of why the timing uses the largest elapsed time
-explanation of what happens to the amount of row calculation per rank as the process count increases
- why communication and packing may limit the speedup


## Organisation strategy
-  on prs say what bullet you hit
- prs need >1 review
- message once pr created to notify team
- review overleaf changes during meetings

## Code styling
- no need for tests/ci
- .clangtidy + ci (chester setups)

## Deadlines

today: 28/10

code completed by wc. 27/11 - by 2nd meeting of that week
job submitted by wc. 30/11 - submit on the first meeting
report completed by wc. 30/11 - submit on the 2nd meeting

deadline: 8/12

## Future meetings
week 8 wc. 2/11
week 9 wc. 9/11 
week 10 wc. 16/11 
week 11 wc. 23/11 
week 12 (deadline to submit) wc. 30/11

mon  
11:30ish
wed
13:30ish

