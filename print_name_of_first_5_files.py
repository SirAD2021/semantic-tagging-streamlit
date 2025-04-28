import os

def main():
    pdf_directory = r'C:\Users\Standard User\OneDrive\Documents\IITJ\MTech\Sem4\VSCode_MTP\pdf_files'
    print("Checking directory existence:", pdf_directory)

    if not os.path.exists(pdf_directory):
        print("Directory does not exist:", pdf_directory)
    else:
        print("Directory exists. Listing the first five PDF files found:")
        pdf_count = 0  # Counter for the number of PDFs printed

        for item in os.listdir(pdf_directory):
            if item.endswith(".pdf"):
                print(item)
                pdf_count += 1
                if pdf_count == 5:
                    break  # Stop after printing five PDF file names

if __name__ == "__main__":
    main()
