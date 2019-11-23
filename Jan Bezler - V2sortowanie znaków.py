litery = "poiuytrewqasdfghjklmnbvcxz"
litery = list(litery)

def babel(ciag):
	dlg = len(ciag)
	for itm in range(dlg-1):
		if ciag[itm] > ciag[itm+1]:	
			ciag[itm],ciag[itm+1]=ciag[itm+1],ciag[itm]
	for itm in range(dlg-1):
		if ciag[itm] > ciag[itm+1]:
			babel(ciag)
	return ciag

print(babel(litery))