function main() {
	console.log("hello, obfuscated world!")
	let total = 0
	for (let i = 0; i < 3; i++) {
		total += i
	}
	return total === 3 ? "ok" : "no"
}

main()
