class Pagination:
    def __init__(self, items=None, page_size=10):
        """
        Initialize the Pagination system.
        :param items: list of items (default is an empty list)
        :param page_size: number of items per page
        """
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  # Zero-based index of the current page

        # Use integer math to calculate total pages (round up)
        self.total_pages = (len(self.items) + self.page_size - 1) // self.page_size

    def get_visible_items(self):
        """
        Returns the list of items currently visible on the current page.
        """
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        """
        Navigates to a specific page number (1-based).
        Raises ValueError if out of range.
        """
        if not isinstance(page_num, int):
            raise ValueError("Page number must be an integer.")
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number out of range. Valid range: 1 to {self.total_pages}")
        self.current_idx = page_num - 1

    def first_page(self):
        """
        Navigates to the first page.
        :return: self (for method chaining)
        """
        self.current_idx = 0
        return self

    def last_page(self):
        """
        Navigates to the last page.
        :return: self (for method chaining)
        """
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        """
        Moves forward one page (if not at last page).
        :return: self (for method chaining)
        """
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        """
        Moves backward one page (if not at first page).
        :return: self (for method chaining)
        """
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        """
        String representation: items on current page, each on a new line.
        """
        return "\n".join(str(item) for item in self.get_visible_items())


#Sample Tests 

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())


p.next_page()
print(p.get_visible_items())


p.last_page()
print(p.get_visible_items())


p.go_to_page(7)
print(p.current_idx + 1)


try:
    p.go_to_page(0)
except ValueError as e:
    print(f"Error: {e}")