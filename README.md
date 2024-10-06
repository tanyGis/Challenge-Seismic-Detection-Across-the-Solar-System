## Challenge-Seismic-Detection-Across-the-Solar-System
Planetary seismology missions struggle with the power requirements necessary to send continuous seismic data back to Earth. But only a fraction of this data is scientifically useful! Instead of sending back all the data collected, what if we could program a lander to distinguish signals from noise, and send back only the data we care about?

In this repository you can find two folders where the processing of seismologic data obtained from the NASA database is applied.

* The first folder (Clean_Data) has the Python file that cleans the data from the incoming noise using a method based on descriptive statistics.

* The second folder (NN_LTA_HUFFMAN) has the Neural Network (Autoencoder) extracting important features and therefore reducing the volume of data. As a solution to the seismic event detection, the preprocessed data goes through a STA/LTA algorithm, allowing the user to detect such events. It also contains a feature that applies a Hoffman compression algorithm to the data obtained through the Neural Network.

Visit the page [here](https://seismicdetectionacrossthesolar.godaddysites.com/#0dee9f89-a6b4-4497-8dca-4bccc0c41d63) to know more about the process.
