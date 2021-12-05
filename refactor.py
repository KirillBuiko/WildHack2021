import tifffile as tiff

a = tiff.imread('data_2/some.tif')
x, y = a.shape[:2]
w = 50
h = 50
W = int(y / w)
H = int(x / h)
count = 0
for i in range(w):
	for j in range(h):
		b = a[(H*i):(H*(i+1)), (W*j):(W*(j+1))]
		flag = False
		corns = [[0, 0],[0, W-1],[H-1, 0],[H-1, W-1]]
		for c in corns:
			q, s, d = b[c[0]][c[1]][:3]
			if(q == 0 and s == 0 and d == 0):
				flag = True
				break
		if(flag == True):
			continue
		if(count%4 == 0):
			tiff.imwrite(f'data_2/img/img_{str(count)}.tif', b)
		count+=1