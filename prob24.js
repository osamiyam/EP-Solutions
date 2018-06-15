
var puts = console.log

function work(){
    var used = []
    for (var i = 0; i < 10; i++) used[i] = false
    var a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var count  = 0
    var N = 1000000

    function det(i){
        if (i >= 10){
            count += 1
            if (count == N){
                puts(a)
                throw("aaa")
	    }
        } else {
            for (var k = 0; k < 10; k++){
                if (!used[k]){
                    used[k] = true
                    a[i] = k
                    det(i + 1)
                    used[k] = false
		}
	    }
	}
    }
    try{
	det(0)
    } catch(e){
    }
}

work()
