async function postData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return response.json();
}

const predict = () => {
  const CHAS = document.querySelector("#CHAS").value;
  const RM = document.querySelector("#RM").value;
  const TAX = document.querySelector("#TAX").value;
  const PTRATIO = document.querySelector("#PTRATIO").value;
  const B = document.querySelector("#B").value;
  const LSTAT = document.querySelector("#LSTAT").value;
  const output = document.querySelector("#output");

  const payload = {
    CHAS: {
      "0": CHAS,
    },
    RM: {
      "0": RM
    },
    TAX: {
      "0": TAX
    },
    PTRATIO: {
      "0": PTRATIO
    },
    B: {
      "0": B
    },
    LSTAT: {
      "0": LSTAT
    },
  };

  postData('http://localhost:8000/predict', payload)
    .then(data => {
      console.log(data);
      output.innerText = data.prediction[0];
    })
    .catch((error) => {
      output.innerHTML = '<span style="color:red">Enter all inputs</span>';
    });
};
