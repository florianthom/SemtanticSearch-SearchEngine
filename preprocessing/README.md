# SemtanticSearch-SearchEngine


### Commands to prepare the first test of the frame work
>This Project aims to build an intelligent seach-engine.<

`conda install nltk`
`python -m nltk.downloader all`

### import or activate german lematization
`conda install -c conda-forge pyphen`
>***Follow the instruction of this guide to import the german lemmatization***<

`git clone https://github.com/WZBSocialScienceCenter/germalemma.git`

>Download from
***http://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/tiger.html***
The Tiger Corpus …. Agree the licence sektion …!!!!
You need only the conll09 format ... extract and run the following statement to create a pickle it ***downsize the bigpack***<

`python germalemma.py tiger_release_aug07.corrected.16012013.conll09`
>create a pickle pack for faster and automated import the set (from 50 MB to 5MB)
