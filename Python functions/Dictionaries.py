#Learning to assign keys and values using dictionaries as buildt-in python function
Bioinfo_career_skills = {'Bioinformatics Analyst': 'Data Analysis', 'Computational Biologist': 'Algorithm Development', 'Genomics Data Scientist': ['NGS', 'pipeline development'], 'Bioinformatics Software Developer': 'coding', 'Scope': 4 }
print(Bioinfo_career_skills)
print(Bioinfo_career_skills['Bioinformatics Analyst'])
print(Bioinfo_career_skills.get('Genomics Data Scientist'))
Bioinfo_career_skills['Proteomics bioinformatician'] = 'Mass spectrometry'
print(Bioinfo_career_skills.get('Proteomics bioinformatician', 'not found'))
print(Bioinfo_career_skills)
Bioinfo_career_skills.update({'Scope': 5, 'words': 'many irrelevant'})
print(Bioinfo_career_skills)
del Bioinfo_career_skills['words']
print(Bioinfo_career_skills)
reduced = Bioinfo_career_skills.pop('Scope')
print(Bioinfo_career_skills)
print(len(Bioinfo_career_skills))
print(Bioinfo_career_skills.items())
print(Bioinfo_career_skills.values())

for careers in Bioinfo_career_skills:
    print(careers)

for careers, skill in Bioinfo_career_skills.items():
    print(careers, skill)


