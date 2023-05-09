import os
files = os.listdir('/storage/udiland/gbib/gbib_data/long_6782_new/220926_longissima_pseudomolecules_v1+unanchored_contigs_split_files')
with open('/storage/udiland/gbib/gbib_data/long_6782_new/220926_longissima_pseudomolecules_v1_un.fasta','w') as f:
	f.write(f">chrUn\n{'N' * 60}\n{'N' * 60}\n{'N' * 60}\n")
	for file in files:
		fas = open(f"/storage/udiland/gbib/gbib_data/long_6782_new/220926_longissima_pseudomolecules_v1+unanchored_contigs_split_files/{file}")
		seq = fas.readlines()
		for line in seq:
			if not line.startswith(">"):
				if len(line) == 61:
					f.write(line)
				else:
					f.write(line.strip())
					f.write(f"{'N' * (61 - len(line))}\n")
		f.write(f"{'N' * 60}\n{'N' * 60}\n{'N' * 60}\n")

