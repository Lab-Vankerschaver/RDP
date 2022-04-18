how to train RDP classifier.

1. make raw DB files to taxonomy and sequence file
Taxonomy file should be tab delimited text file. Each line contains one species with 8 items: seq_ID, kingdom, phylum, ... , species.

Seq_ID	Kingdom	Phylum	Class	Order	Family	Genus	Species
4321924	Bacteria	Actinobacteria	Actinobacteria	Actinomycetales	Corynebacteriaceae	Corynebacterium	durum
1042479	Bacteria	Bacteroidetes	Bacteroidia	Bacteroidales	Prevotellaceae	Prevotella	melaninogenica

Sequence file should be fasta format without enter in each sequence.

>4321924
GAGTTTGA...
>1042479
GATGAAAA...

- input file format is csv, use csv2taxseq.py

code →
python /path/to/csv2taxseq.py /path/to/DB_dataset.csv /path/to/DB/raw_taxonomy.txt /path/to/DB/raw_sequences.fasta

2. make input file for RDP
code →
- python /path/to/lineage2taxTrain.py /path/to/DB/raw_taxonomy.txt > /path/to/DB/ready4train_taxonomy.txt

0*Root*-1*0*rootrank
1*Bacteria*0*1*Kingdom
2*Actinobacteria*1*2*Phylum
3*Actinobacteria*2*3*Class
4*Actinomycetales*3*4*Order
5*Corynebacteriaceae*4*5*Family
6*Corynebacterium*5*6*Genus
7*durum*6*7*Species

- python /path/to/addFullLineage.py /path/to/DB/raw_taxonomy.txt /path/to/DB/raw_sequences.fasta > /path/to/DB/ready4train_seqs.fasta

>4321924	Root;Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Corynebacteriaceae;Corynebacterium;durum
GAGTTTGAT...
>1042479	Root;Bacteria;Bacteroidetes;Bacteroidia;Bacteroidales;Prevotellaceae;Prevotella;melaninogenica
GATGAACG...

3. TRAIN
code →
- java -Xmx10g -jar /path/to/classifier.jar train -o /path/to/DB/training_files -s /path/to/DB/ready4train_seqs.fasta -t /path/to/DB/ready4train_taxonomy.txt
- cp /path/to/DB/traing_files/rRNAClassifier.properties /path/to/training_files/
  - rRNAClassifier.properties should be located in same folder with training_files

4. Classify with new trained model
code →
java -Xmx1g -jar /path/to/classifier.jar classify -t /path/to/DB/training_files/rRNAClassifier.properties -o output_classified.txt /path/to/DB/ready4train_seqs.fasta.