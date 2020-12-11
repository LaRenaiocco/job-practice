// return the min and max of an array as an array [min, max]

function minMax(arr) {
	const minNum = Math.min(...arr);
	const maxNum = Math.max(...arr);
	const result = [minNum, maxNum];
	return result;
}

//  f and g are functions that take no arguments and return an integer
//  find with returns a larger integer and return 'f', 'g' or 'neither'
function whichIsLarger(f, g) {
	const fResult = f()
	const gResult = g()
	if (fResult > gResult) {
		return 'f'
	} else if ( gResult > fResult) {
		return 'g'
	} else {
		return 'neither'
	}
}

//  mimic the left shift operator in JS without using left shift
function shiftToLeft(x, y) {
	const leftShift = 2 ** y
	return x * leftShift
}