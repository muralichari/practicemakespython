def even_list(N):
      L = []
      for i in range(0,N+1,2):
            if i%2 == 0:
                L.append(i)
      return L
    
Listing = even_list(10)
print(Listing)