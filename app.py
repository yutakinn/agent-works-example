import streamlit as st

def main():
    st.title("案件例生成システム")

    job_examples = []

    with st.form("job_example_form"):
        for i in range(10):
            st.subheader(f"案件 {i+1}")
            language = st.text_input(f"言語を入力 {i+1}", "")
            project_name = st.text_input(f"案件名を入力 {i+1}", "")
            price = st.number_input(f"単価を入力（例：800,000） {i+1}", min_value=0, max_value=10000000, value=0, step=10000)
            feature1 = st.text_input(f"1つ目の特徴 {i+1}", "")
            feature2 = st.text_input(f"2つ目の特徴 {i+1}", "")
            job_examples.append((language, project_name, price, feature1, feature2))

        submitted = st.form_submit_button("案件例を生成")

    if submitted:
        job_examples_html = generate_job_examples_html(job_examples)
        st.code(job_examples_html, language='html')

def generate_job_examples_html(job_examples):
    job_examples_html = '''

<div class="job-examples-container">
  <div class="job-examples">
'''

    for job in job_examples:
        language, project_name, price, feature1, feature2 = job
        formatted_price = f"{price:,.0f}"  # カンマ区切りの数値形式に変換
        job_example_html = f'''
        <div class="job-example">
            <p class="job-category">{language}</p>
            <p class="job-title">{project_name}</p>
            <div class="job-details">
                <span class="salary"><i class="fas fa-yen-sign"></i>〜<span class="amount">{formatted_price}</span>円/月</span>
            </div>
            <div class="job-tags">
                <span>{feature1}</span>
                <span>{feature2}</span>
            </div>
        </div>
        '''
        job_examples_html += job_example_html

    job_examples_html += '''
  </div>
  <div class="show-more">
    <button>もっと見る</button>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const jobExamplesContainers = document.querySelectorAll('.job-examples-container');

  jobExamplesContainers.forEach(container => {
    const showMoreBtn = container.querySelector('.show-more button');
    const hiddenExamples = container.querySelectorAll('.job-example:nth-child(n+5)');

    showMoreBtn.addEventListener('click', () => {
      hiddenExamples.forEach(example => {
        example.style.display = 'block';
      });
      showMoreBtn.style.display = 'none';
    });
  });
});
</script>
'''

    return job_examples_html

if __name__ == "__main__":
    main()