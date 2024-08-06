import styles from './Search.module.css';

import { useState } from 'react';

import 'gridjs/dist/theme/mermaid.css';
import { Grid } from 'gridjs-react';

export default function Search(){
  const [dataGrid, setDataGrid] = useState([
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
    ['John', 'john@example.com'],
  ]);

  const columnsGrid = ['Name', 'Email'];

  const stylingGrid = {
    container: `${styles.containerGrid}`,
    header: `${styles.header}`,
    search: `${styles.searchGrid}`,
    th: `${styles.th}`,
    td: `${styles.td}`,
    footer: `${styles.footer}`,
  };

  return(
    <section className={styles.container}>
      <h1 className={styles.pageTitle}>Search</h1>
      <Grid
        data={dataGrid}
        columns={columnsGrid}
        search={true}
        pagination={{
          limit: 10,
        }}
        className={stylingGrid}
      />
    </section>
  );
};