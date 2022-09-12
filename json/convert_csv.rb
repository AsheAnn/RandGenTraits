# frozen_string_literal: true

require 'csv'

table = CSV.parse(File.read(Dir.home + '/tmp/RandGenTraits/csv/00.csv'), headers: true)

index_percent = []
[*1..34].each do |i|
  index_percent.push(table.by_col[i].compact.map(&:to_f))
end

puts index_percent.inspect
puts table.by_col[0].compact.map(&:to_f).inspect
