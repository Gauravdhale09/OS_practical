MAX_FRAMES = 3
MAX_PAGES = 20

def is_page_exists(frame, page_number):
    return page_number in frame

def display_frame(frame):
    for page in frame:
        if page == -1:
            print("- ", end="")
        else:
            print(f"{page} ", end="")
    print()

def main():
    page_sequence = [1, 2, 3, 4, 5, 2, 1, 6, 7, 8, 7, 8, 9, 3, 4, 5, 6, 9, 1, 2]
    frame = [-1] * MAX_FRAMES
    page_faults = 0
    current_index = 0

    print("Page Sequence:", " ".join(str(page) for page in page_sequence), "\n")

    print("FIFO Page Replacement Algorithm:")
    for page in page_sequence:
        print(f"Page {page} -> Frame: ", end="")
        if not is_page_exists(frame, page):
            frame[current_index] = page
            current_index = (current_index + 1) % MAX_FRAMES
            page_faults += 1
        display_frame(frame)

    print("\nTotal Page Faults:", page_faults)

if __name__ == "__main__":
    main()
