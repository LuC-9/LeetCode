class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # this regex has two group: 
		# 1. a file name group 
		# 2. a content group
		#
		# Ex: "root/a 1.txt(abcd) 2.txt(efgh)"
		# 
		# Output: [('1.txt', 'abcd'), ('2.txt', 'efgh')]
        content_regex = re.compile("(\w+.txt)\((.*?)\)", re.IGNORECASE)
		
		# hashmap to keep everything
		#
        d = defaultdict(list)
		
		# go through each path
		# 
        for path in paths:
			
			# a regex expression is not needed as the dir path
			# is always the first item and is seperated by a space
			#
            root = path.split(" ")[0]
            file = re.findall(content_regex, path)
            
            for file_name, content in file:
                
				# store a list of file plus its directory under the content of each file
				#
                d[content].append(root + "/" + file_name)            
        
		# filtering out anything that has a length that is smaller than 1
		# since it wouldn't be a group
		#
        return list(filter(lambda x: len(x) > 1, d.values())) 
        