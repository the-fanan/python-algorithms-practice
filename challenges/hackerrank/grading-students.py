#EASY

#if difference between grade and next multiple of 5 is less than 3 add scores to make grade next multiple of 5 
#else leave as is
#if grade is less than 38, leave as is

# grades array 
for idx, grade in enumerate(grades):
	if not (grade < 38 or grade % 5 < 3):
		grades[idx] = grade + (5 - (grade %5 ))
	return grades  