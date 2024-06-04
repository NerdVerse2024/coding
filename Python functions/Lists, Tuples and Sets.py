# List of strings and integers
courses = ['Molecular biology', 'Bioinformatics', 'Genomics', 'Cell Biology']
courses_2 = ['Transcriptomics', 'Cancer Genomics']
print(courses)
print(len(courses))
print(courses[2])
print(courses[-1])
print(courses[0:3])
print(courses[:3])
print(courses[1:])
courses.append('Metagenomics')
print(courses)
courses.insert(2, 'Single cell genomics')
print(courses)
courses.extend(courses_2)
print(courses)
courses.remove('Cell Biology')
print(courses)
popped = courses.pop()
print(courses)
print(popped)
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
sorted_C = sorted(courses)
print(sorted_C)
numbers = [23, 9859, 53, 32523, 698, 23436] 
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
sorted_1 = sorted(numbers)
print(sorted_1)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(courses.index('Bioinformatics'))
print('art' in courses)
print('Metagenomics' in courses)
for item in courses: 
    print(item)
for index,coursename in enumerate(courses):
    print(index, coursename)

courses_str = ', '.join(courses)
print(courses)
course_splt = courses_str.split(' - ')
print(courses_str)
print(course_splt)


##Tuples [The immutable ones]
BIOINFO_TOOLS_TUPLES1 = ('BLAST', 'GPROFILER', 'TRIMMOMATICS', 'FEATURECOUNTS')
BIOINFO_TOOLS_TUPLES2 = BIOINFO_TOOLS_TUPLES1
print(BIOINFO_TOOLS_TUPLES1)
print(BIOINFO_TOOLS_TUPLES2)
#BIOINFO_TOOLS_TUPLES1[0] = 'BLASTX' {CAN'T DO THAT, RUNNING THIS WILL THROW AN ERROR}

## Sets 
bioinfo_database_sets = {'UCSC', 'RNACENTRAL', 'NCBI', 'PDB', 'UCSC'} #IT THROWS AWAY DUPLICATES
bioinfo_ncrna_sets = {'GEO', 'NCBI', 'RNACENTRAL', 'NONCODE'}
print(bioinfo_database_sets)
print('PDB' in bioinfo_database_sets)
print(bioinfo_database_sets.intersection(bioinfo_ncrna_sets))
print(bioinfo_database_sets.difference(bioinfo_ncrna_sets))
print(bioinfo_database_sets.union(bioinfo_ncrna_sets))

##Creating empty lists, tuples and sets 
empty_list = []
empty_list2 = list()

tuple_empty = ()
tuple_empty2 = tuple()

empty_set = set()