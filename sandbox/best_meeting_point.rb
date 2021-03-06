require 'set'
def min_total_distance(grid)
    return 0 if grid.empty? || grid[0].empty?

    m, n = grid.size, grid[0].size          # count is the count of nodes
    d = Array.new(m) { Array.new(n, 0) }    # Matrix of sum of distances from buildings to each point in grid

    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            next if grid[i][j] != 1 # We do BFS only from each building
            bfs(grid, i, j, d)
        end
    end

    min_dist = Float::INFINITY
    0.upto(m - 1) do |i|
        0.upto(n - 1) do |j|
            min_dist = [min_dist, d[i][j]].min
        end
    end

    min_dist == Float::INFINITY ? -1 : min_dist
end


def bfs(grid, start_x, start_y, d)
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    m, n = grid.size, grid[0].size
    q, visited = [[start_x, start_y, 0]], Set.new([[start_x, start_y]])

    while !q.empty?
        x, y, dist = q.shift()
        dirs.each do |di, dj|
            i, j = x + di, y + dj
            next if !i.between?(0, m - 1) || !j.between?(0, n - 1) || visited.include?([i, j])
            visited.add([i, j])
            q.push([i, j, dist + 1])
            d[i][j] += dist + 1
        end
    end
end





# 296. Best Meeting Point
# https://leetcode.com/problems/best-meeting-point/description/

# Manhattan distance: 


require 'test/unit'
extend Test::Unit::Assertions

grid = [[0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0],
[0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0],
[0,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0],
[0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0],
[1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0],
[0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1],
[0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
[1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0],
[0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0],
[1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0],
[0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0],
[1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0],
[0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,0],
[0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
[1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
[0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0],
[0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0],
[1,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0],
[1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
[0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
[1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,1],
[1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0],
[0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1],
[0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0],
[0,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0],
[0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,0],
[0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1]]


assert_equal(min_total_distance(grid), 2070)
