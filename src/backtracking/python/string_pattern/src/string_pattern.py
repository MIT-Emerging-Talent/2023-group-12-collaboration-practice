def string_pattern(string, pattern):
    def dfs(i, j, mapping, reverse_mapping):
        if i == len(string) and j == len(pattern):
            return True
        if i == len(string) or j == len(pattern):
            return False

        current_pattern_char = pattern[j]

        if current_pattern_char in mapping:
            mapped_str = mapping[current_pattern_char]
            if not string.startswith(mapped_str, i):
                return False
            return dfs(i + len(mapped_str), j + 1, mapping, reverse_mapping)

        for k in range(i, len(string)):
            substring = string[i:k + 1]
            if substring not in reverse_mapping:
                mapping[current_pattern_char] = substring
                reverse_mapping.add(substring)

                if dfs(k + 1, j + 1, mapping, reverse_mapping):
                    return True

                del mapping[current_pattern_char]
                reverse_mapping.remove(substring)

        return False

    mapping = {}  # Mapping from pattern characters to substrings in string
    reverse_mapping = set()  # Set of substrings in string that have been mapped

    return dfs(0, 0, mapping, reverse_mapping)
