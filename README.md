TimeTable Creator

This nifty program aims to create Full Fedged Clash Free timetable For BITS Pilani students.
Data is sourced from the Timetable Booklets given to us at the start of the semester.

The Data is stored in various Excel sheets in the /Timetable folder

The codes for data processing are given below:

----------------------------------------------------------------------------------------------------------------------------------------------------

Manual tweking was required in the timetable file so that common hour data was applied to all the sections that
required it but didn't have it mentioned(Only mentioned on the first line of sections).

Might code this later.

----------------------------------------------------------------------------------------------------------------------------------------------------

Step 1:
Name_Attacher.py:

This code does the job of taking the names of instructors that teach the same section 
which is present on more than one row of the ecxcel sheet and merge them in a comma seperated
form so that each row of the excel sheet has an assocaiated section
Eg.

1002	BIO F111	GENERAL BIOLOGY	3	0	3	1	RAJDEEP CHOWDHURY (229)	                        5105	M W F	9				11/12    AN
							                        Manoj Kannan (393)							
						                        2	Manoj Kannan (393)	                            5105	T Th S	4				
							                        Rajdeep Chowdhury (229)	

 to

1002	BIO F111	GENERAL BIOLOGY	3	0	3	1	RAJDEEP CHOWDHURY (229), Manoj Kannan (393)	    5105	M W F	9				11/12    AN
						                        2	Manoj Kannan (393), Rajdeep Chowdhury (229)	    5105	T Th S	4

----------------------------------------------------------------------------------------------------------------------------------------------------

Step 2:
Labeller.py:

This code does the job of prepend the type of class Lecture 'L', Practical 'P' and Tutorial 'T'
to the section number so that each row of the table has a combined code like L1, T6 or P4.
Project Type courses(which do not have section number) have a a code 'PR0'
Eg.

1001	BIO F110	BIOLOGY LABORATORY	0	2	1	1	BHAGAVATULA VANI (904)	    3219	T	1 2	M	1	6163	30/11    FN
						                            2	Neelam Mahala (RS) (628)	3219	M	3 4	M	1		
						                            3	Meghana Tare (599)	        3219	M	6 7	M	1		
						                            4	Sumukh Thakar (RS) (1,065)	3219	M	8 9	M	1		
						                            5	Anirudh Sahu (RS) (786)	    3219	M	1 2	M	1		
						                            6	Tripti Mishra (RS) (200)	3219	T	3 4	M	1		

 to

1001	BIO F110	BIOLOGY LABORATORY	0	2	1	P1	BHAGAVATULA VANI (904)	    3219	T	1 2	M	1	6163	30/11    FN
						                            P2	Neelam Mahala (RS) (628)	3219	M	3 4	M	1		
						                            P3	Meghana Tare (599)	        3219	M	6 7	M	1		
						                            P4	Sumukh Thakar (RS) (1,065)	3219	M	8 9	M	1		
						                            P5	Anirudh Sahu (RS) (786)	    3219	M	1 2	M	1		
						                            P6	Tripti Mishra (RS) (200)	3219	T	3 4	M	1	
----------------------------------------------------------------------------------------------------------------------------------------------------

Step 3:
TTSEQ_Generator.py:

This code does the job of taking the Day and Hour (including Common Hour) of a particular section
and entering 1's in their respective locations on a 6X11 matrix, representing a weeky timetable.
The locations of 1's represents the timetable slots that would be filled on selection of that particular section.

Eg.
DAYS:	['T', 'Th', 'S']
HOURS:	['2']
TTSEQ:	[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 	[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 	[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 	[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 	[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 	[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

----------------------------------------------------------------------------------------------------------------------------------------------------
