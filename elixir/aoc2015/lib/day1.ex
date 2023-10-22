defmodule Day1 do
  @file_name "../../../inputs/2015/day1.txt"
  def read_file(file_name \\ @file_name) do
    {_, content} = File.read(file_name)
    String.trim(content)
  end

  def move_santa("(" <> rest, floor, character) do
    move_santa(rest, floor + 1, character + 1)
  end

  def move_santa(")" <> rest, floor, character) do
    case floor do
      -1 -> 
        IO.puts("PART2 solution: #{character}") 
        move_santa(rest, floor - 1, character + 1)
      _ -> move_santa(rest, floor - 1, character + 1)
    end
  end
  def move_santa("" <> _rest, floor, _character) do
    IO.puts("PART1 solution: #{floor} ")
  end
end

Day1.read_file
|> Day1.move_santa(0, 0)


