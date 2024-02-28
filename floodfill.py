def floodFill(image: List[List[int]], sr: int, sc: int, color: int):

        check_color = image[sr][sc]
        visited = []
        m = len(image)
        n = len(image[0])

        def backtracking(image, r, c):
            if image[r][c] == color:
                return
            else:
                if image[r][c] == check_color:
                    image[r][c] = color
                    visited.append((r,c))
                    if r+1 <= m-1 and (r+1,c) not in visited:
                        backtracking(image, r+1, c)
                    if c+1 <= n-1 and (r,c+1) not in visited:
                        backtracking(image, r, c+1)
                    if r-1 >= 0 and (r-1,c) not in visited:
                        backtracking(image, r-1, c)
                    if c-1 >= 0 and (r,c-1) not in visited:
                        backtracking(image, r, c-1)
                    visited.remove((r,c))

        backtracking(image,sr,sc)
        return image
