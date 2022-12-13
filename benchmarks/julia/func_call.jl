repeat = 100
number = 1000

function add(x, y)
    return x + y

end

function mul(x, y)
    return x * y

end

function geom_mean(x, y)
    return add(x, y) / (mul(x, y) + 1)
end

function func_a()
    for i in 1:number
        x = 9000
        for y in 1:100
            result = geom_mean(x, y)

        end
    end

end

function func_b()
    for i in 1:number
        x = 9000
        for y in 1:100
            result = (x + y) / (x * y + 1)
        end
    end

end
@time func_a()
@time func_b()