# # with open('input.inp','r') as filein:
# #     ten=filein.readline().rstrip('\n')
# #     tuoi=int(filein.readline().rstrip('\n'))

# # with open('output.outp','w') as output:
# #     output.write('PCL la so 1 ahihi')

#Mo file voi mode='r' de doc file
with open('input.inp.txt', 'r') as fileInp:

   #Doc 1 dong du lieu tu file va luu vao bien ten
   #Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
   ten = fileInp.readline().rstrip('\n')

   #Doc 1 dong du lieu tu file va luu vao bien tuoiHienTai
   tuoiHienTai = int(fileInp.readline())

#Mo file voi mode='w' de ghi file
with open('Bai1.10.out.txt', 'w') as fileOut:

   #Ghi noi dung vao file theo mau
   fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))
   fileOut.write("\nLap dep trai nhat he mat troi")