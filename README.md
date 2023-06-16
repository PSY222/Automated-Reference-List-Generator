# Automated-Reference-List-Generator
Quick and simple reference list generator that extracts information from pdf files inside a given folder. 

## Quick facts about this generator
- This generator automatically extracts information from pdf files located inside a given [folder path].
- Current reference format follows IEEE format like "[reference number] {author}. {title}, {published year}"
- (Feel free to change the format to APA,MLA, Harvard Referencing format or etc.)

### Expected out comes
```
References
[1] Pedro Martins, José Silvestre Silva and Alexandre Bernardino. Multispectral Facial Recognition in the Wild, 2022 ```

## 📌Limitations
- Author and title are extracted based on the first/second line of the document unless proper metadata is provided. Therefore, it is important to double-check the details after generating the reference draft using this generator.
- If your title is over one line, you should edit the title.
- It was challenging to extract publication information such as volume, issue, or other relevant details from the documents due to the varying formats of research papers.
- But, I am sure that this can be very simple but useful reference list generator for those who keep the referred PDF documents to the folder 📚

## How to use this repo 🖐
1. git clone [this repo HTTPS code]
2. Navigate to this repo
```cd Automated-Reference-List-Generator```
3. Type the command
```python pdf2ref.py -f [folder path] -o [output path to save txt file] ```