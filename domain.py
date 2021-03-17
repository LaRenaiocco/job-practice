# Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string.

def domain_name(url):
    """ 
    >>> domain_name("http://github.com/carbonfive/raygun")
    'github'
    >>> domain_name("http://www.zombie-bites.com")
    'zombie-bites'
    >>> domain_name("https://www.cnet.com")
    'cnet'
    >>> domain_name("www.xakep.ru")
    'xakep'
    >>> domain_name("buffy.com") 
    'buffy'
    """
    if url.startswith('http'):
        url_list = url.split('//')
        if url_list[1].startswith('www'):
            one_list = url_list[1].split('.')
            return one_list[1]
        else:
            one_list = url_list[1].split('.')
            return one_list[0]
    elif url.startswith('www'):
        url_list = url.split('.')
        return url_list[1]
    else:
        url_list = url.split('.')
        return url_list[0]

# Much more eloquent version!!!
#  return url.split("//")[-1].split("www.")[-1].split(".")[0]



# pseudocode:
# possible starts of input == http and www
# if start with http:
#     split on '//'
#     look at index 1
#     if starts with www, split on .
#     return index 1
# if starts with a www
#     split on .
#     return index 1
# else
#     split on .
#     return index 0




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')