These scripts are provided open source and is designed to aid libraries and archives in building deep linked data networks for image collections based on AI (opencv) processing of digital/digitized images and associated metadata csv files.  
Start - Image Segmentation
- Boxing Images
- (ClearRAM is provided due to Jupyter's issues with clearing RAM - use if you recieve an out of RAM error)
- boxes
- csv_to_triples
-> Can utilize OpenRefine at this point to connect to wikidata for common proper nouns and use the inbuilt disambiguation tools
- hive

The output is a series of cropped images of people depicted in the collection, as well as the initial list of triple URIs associated with each original image ready for use with Mediawiki or another linked data web tool.  These webs are not perfect and humans will certainly be able to build additional connections quickly from the initial machine-generated web, however, the automation saves a lot of time by converting already captured metadata to ready to use entities and relations.
