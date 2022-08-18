const colorPercent17 = [2, 2, 5, 1, 15, 5, 1, 2, 3, 10, 5, 5, 18, 5, 11, 5, 5]

const colorPercent20 = [
  2, 2, 5, 1, 12, 5, 1, 2, 3, 10, 5, 5, 10, 5, 7, 5, 5, 5, 5, 5,
]
const percent = [
  1, 1, 3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3,
  3, 3, 3, 3, 3, 3, 2, 3,
]

const hairFirstHalf = [...new Array(19)].map((val, index) => {
  const hairColor1 = [...new Array(17)].map((val, index) => {
    const colorObj1 = {
      index: index + 1,
      name: "",
      percent: colorPercent17[index],
    }
    return colorObj1
  })
  return hairColor1
})

const hairLastHalf = [...new Array(14)].map((val, index) => {
  const hairColor2 = [...new Array(20)].map((val, index) => {
    const colorObj2 = {
      index: index + 1,
      name: "",
      percent: colorPercent20[index],
    }
    return colorObj2
  })
  return hairColor2
})

const allData = hairFirstHalf.concat(hairLastHalf)

const hair = [...new Array(33)].map((val, index) => {
  const obj = {
    index: index,
    percent: percent[index],
    color: allData[index],
  }
  return obj
})

console.log(JSON.stringify(hair))
