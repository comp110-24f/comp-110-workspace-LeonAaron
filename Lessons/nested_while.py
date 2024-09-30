"""Practice for the unit 1 quiz"""


def num_instances(inp_str: str, search_str: str):
    """Counts num of instances of search_str in inp_str"""

    # initialize variables
    count: int = 0
    index: int = 0

    while index <= len(inp_str) - len(search_str):

        sub_index: int = 0
        match: bool = True

        while sub_index < len(search_str):
            if inp_str[index + sub_index] != search_str[sub_index]:
                match = False
            sub_index += 1

            if match:
                count += 1
                index += len(search_str)
            elif not match:
                index += 1

    print(count)


num_instances(inp_str="HelloHello", search_str="Hello")
