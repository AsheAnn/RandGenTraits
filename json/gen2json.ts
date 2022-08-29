const randomPercents = (amount, totalPercent) => {
  const randomArray = [...new Array(amount)].map(() => {
    return Math.random() * 10
  })
  const sum = randomArray.reduce((a, b) => a + b, 0)
  return randomArray.map((val) =>
    Number(((val / sum) * totalPercent).toFixed(2))
  )
}

const handPercent = randomPercents(27, 100)
const neckPercent = randomPercents(48, 100)

const hand = [
  20, 3, 3, 2, 4, 4, 2, 3.8, 5, 1, 4, 3.8, 1, 3.8, 4, 3.8, 2, 3.8, 1, 3.8, 3.8,
  3.8, 1, 2, 1, 3.8, 5.8,
]

const neck = [
  10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 2, 2, 3, 2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2,
  1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2,
]

const generateToJson = (array) => {
  const dataList = [...new Array(array.length)].map((_val, index) => {
    const dataObj = {
      index: index,
      percent: array[index],
    }
    return dataObj
  })
  console.log(JSON.stringify(dataList))
}

// generateToJson(hand)
// generateToJson(neck)


const generateBodyToJson = (typeArray, idxArray) => {
  const subList  = [...new Array(idxArray.length)].map((_val, index) => {
    const obj = {
      index: index + 1,
      percent: idxArray[index],
    }
    return obj
  })
  const mainList = [...new Array(typeArray.length)].map((_val, index) => {
    const dataObj = {
      index: index + 1,
      percent: typeArray[index],
      color: subList[index],
    }
    return dataObj
  })
  console.log(JSON.stringify(mainList))
}

const bodyTypePercent = [20, 20, 10, 10, 20, 20]
const bodyIndexPercent = [2, 2, 1, 1, 2, 2, 10, 2, 28, 30, 20]

generateBodyToJson(bodyTypePercent, bodyIndexPercent)


