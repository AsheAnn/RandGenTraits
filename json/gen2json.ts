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
  const subList = [...new Array(idxArray.length)].map((_val, index) => {
    const idxPercent = idxArray[index]
    const percentList = [...new Array(idxArray[index].length)].map(
      (_val, index) => {
        const obj = {
          index: index + 1,
          percent: idxPercent[index],
        }
        return obj
      }
    )
    return percentList
  })

  const mainList = [...new Array(typeArray.length)].map((_val, index) => {
    const dataObj = {
      index: index + 1,
      percent: typeArray[index],
      color: subList[index],
    }
    return dataObj
  })

  const traits = [
    {
      name: 'Body',
      count: typeArray.length,
      type: mainList,
    },
  ]

  const finalObj = {
    seed: 1000,
    traits: traits,
  }

  console.log(JSON.stringify(finalObj))
}

const bodyTypePercent = [
  15.0, 3.0, 7.0, 2.0, 4.5, 2.5, 2.0, 0.2, 2.5, 3.0, 2.5, 1.0, 2.5, 2.0, 2.5,
  0.1, 0.1, 2.5, 5.0, 2.5, 2.5, 2.0, 2.0, 2.0, 5.0, 0.1, 2.0, 2.0, 3.0, 2.0,
  3.0, 5.0, 3.0, 4.0,
]

const bodyIndexPercent = [
  [
    4.0, 3.0, 3.0, 2.0, 1.0, 4.0, 1.0, 2.0, 1.0, 5.0, 1.0, 3.0, 1.0, 3.0, 5.0,
    2.0, 1.0, 2.0, 1.0, 2.0, 5.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 4.0, 1.0,
    1.0, 1.0, 1.0, 6.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
  ],
  [15.0, 10.0, 6.0, 7.0, 3.0, 8.0, 15.0, 7.0, 9.0, 4.0, 10.0, 3.0, 2.0, 1.0],
  [
    10.0, 7.0, 15.0, 5.0, 15.0, 5.0, 10.0, 5.0, 8.0, 9.0, 3.0, 2.0, 1.0, 2.0,
    3.0, 4.0, 1.0, 3.0, 2.0, 1.0,
  ],
  [15.0, 4.0, 18.0, 6.0, 2.0, 10.0, 4.0, 8.0, 12.0, 2.0, 10.0, 9.0],
  [20.0, 12.0, 20.0, 2.0, 28.0, 18.0],
  [20.0, 4.0, 16.0, 4.0, 10.0, 28.0, 16.0, 2.0],
  [8.0, 10.0, 18.0, 10.0, 2.0, 7.0, 15.0, 10.0, 20.0],
  [50.0, 20.0, 20.0, 10.0],
  [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
  [
    9.0, 5.0, 15.0, 5.0, 10.0, 5.0, 10.0, 5.0, 1.0, 10.0, 7.0, 8.0, 5.0, 2.0,
    3.0, 2.0,
  ],
  [10.0, 4.0, 10.0, 10.0, 10.0, 10.0, 6.0, 10.0, 10.0, 10.0, 10.0],
  [25.0, 15.0, 15.0, 20.0, 15.0, 10.0],
  [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 20.0],
  [15.0, 25.0, 15.0, 20.0, 15.0, 10.0],
  [10.0, 20.0, 10.0, 10.0, 10.0, 10.0, 20.0, 10.0],
  [100.0],
  [100.0],
  [2.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 4.0, 10.0, 10.0, 4.0],
  [10.0, 7.0, 15.0, 5.0, 15.0, 5.0, 10.0, 5.0, 12.0, 9.0, 3.0, 2.0, 1.0, 1.0],
  [2.0, 12.0, 20.0, 12.0, 14.0, 14.0, 26.0],
  [2.0, 12.0, 16.0, 30.0, 10.0, 14.0, 16.0],
  [11.0, 25.0, 16.0, 2.0, 30.0, 15.0, 1.0],
  [1.0, 15.0, 15.0, 30.0, 10.0, 14.0, 15.0],
  [1.0, 15.0, 15.0, 30.0, 10.0, 14.0, 15.0],
  [15.0, 10.0, 10.0, 1.0, 3.0, 8.0, 15.0, 7.0, 1.0, 12.0, 10.0, 5.0, 2.0, 1.0],
  [50.0, 50.0],
  [35.0, 40.0, 10.0, 10.0, 5.0],
  [25.0, 25.0, 25.0, 25.0],
  [20.0, 10.0, 10.0, 1.0, 10.0, 10.0, 10.0, 15.0, 4.0, 10.0],
  [4.0, 10.0, 10.0, 1.0, 10.0, 15.0, 10.0, 15.0, 10.0, 15.0],
  [4.0, 10.0, 10.0, 5.0, 1.0, 15.0, 10.0, 15.0, 10.0, 15.0, 5.0],
  [10.0, 10.0, 4.0, 5.0, 5.0, 10.0, 15.0, 15.0, 10.0, 15.0, 1.0],
  [10.0, 20.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
  [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0],
]

generateBodyToJson(bodyTypePercent, bodyIndexPercent)
