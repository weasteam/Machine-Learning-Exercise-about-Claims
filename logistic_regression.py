# Perform the prediction with logistic regression

# import the packages
#from sklearn import svm, cross_validation
import numpy as np
import sys

# public values
y_negative = ["F13", "J8G", "JO5", "JB8", "JE1", "JC9", "JF1", "JF9", "JG1", "JPA", "JES"]

def clean_cell(cell):
	print cell
	if str(cell).find("\"") != -1: # string
		cell = str(cell).replace("\"","")
		if cell == " ":
			cell = np.nan
	elif str(cell).find("\.") == -1: # float
		cell = int(cell)
	else:#int
		cell=float(cell)
	return cell

def clean_y(cell):
	cell = str(cell).replace("\"","")
	if cell in y_negative:
		return 1
	else:
		if cell == ' ':
			return np.nan
		else:
			return 0

# Main program
def main():
	print "Reading CSV file..."
	data = np.genfromtxt('claim.sample.csv', delimiter=',',dtype=None)
	print "Removing the title line..."
	title = data[0]
	data = data[1:,:]
	print "Data shape: %s" % data.shape
	print data[0,:]
	print "Getting y..."
	y = data[:,12]
	print "Preparing the Y value"
	Y = [clean_y(i) for i in y]
	print "Removing nan rows..."
	idx = np.where(np.isnan(np.array(Y)) == False)[0]
	data_sub = data[idx,:]
	Y_sub = np.array(Y)[idx]
	print "Remaining shpae %s" % data_sub.shape
	print "Removing unnecessary columns"
	print "Removing ID(0),Denial.Reason.Code(12)"
	idx_col = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
	x_sub = data_sub[:,idx_col]
	title_sub = title[idx_col]
	print "Positive date: %s" % len(np.where(Y_sub == 1)[0])
	print "Negative date: %s" % len(np.where(Y_sub == 0)[0])
	print "Unique value of each column"
	i = 0
	while i < len(title_sub):
		print "%s unique count: %s" % (title_sub[i],len(np.unique(x_sub[:,i])))
		i += 1
	# "Claim.Number" unique count: 33152
	# "Claim.Line.Number" unique count: 135
	# "Member.ID" unique count: 11799
	# "Provider.ID" unique count: 26
	# "Line.Of.Business.ID" unique count: 6
	# "Revenue.Code" unique count: 161
	# "Service.Code" unique count: 112
	# "Place.Of.Service.Code" unique count: 3
	# "Procedure.Code" unique count: 2918
	# "Diagnosis.Code" unique count: 2501
	# "Claim.Charge.Amount" unique count: 14180
	# "Price.Index" unique count: 3
	# "In.Out.Of.Network" unique count: 3
	# "Reference.Index" unique count: 3
	# "Pricing.Index" unique count: 4
	# "Capitation.Index" unique count: 3
	# "Subscriber.Payment.Amount" unique count: 33
	# "Provider.Payment.Amount" unique count: 25054
	# "Group.Index" unique count: 1280
	# "Subscriber.Index" unique count: 10996
	# "Subgroup.Index" unique count: 1287
	# "Claim.Type" unique count: 2
	# "Claim.Subscriber.Type" unique count: 2
	# "Claim.Pre.Prince.Index" unique count: 3
	# "Claim.Current.Status" unique count: 7
	# "Network.ID" unique count: 16
	# "Agreement.ID" unique count: 29
	print "Cleaning the data..."
	for x in np.nditer(data, op_flags=['readwrite']):
		x[...] = clean_cell(x)
	# scale
	# normalize, if not well distribute
	print data[1,:]


if __name__ == '__main__':
	main()
