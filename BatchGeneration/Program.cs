// Copyright Titus Thompson, 2025. All Rights Reserved.

namespace BatchGeneration;

class Program
{
    static String ROOT_FOLDER = @"X:\XXXXXXXXXXXXXXXXXXXXXXX\PuzzleImageGen\";
    static String OUTPUT_PATH = @"BatchGeneration\output\S1\";

    static void Main(string[] args)
    {
        BatchGenerator bg = new BatchGenerator(1, "S1", @"Group_Sn\Sn_Generation.py");
        bg.GenerateAll();
    }

    public class BatchGenerator
    {
        int ordinal;
        String groupName;

        string rootFolder = ROOT_FOLDER;
        string binPath = @"BatchGeneration\bin\Debug\net7.0\media\images";
        string outputPath = OUTPUT_PATH;
        string pythonCmd;

        public BatchGenerator(int ordinal, String groupName, String pythonPath)
        {
            this.ordinal = ordinal;
            this.groupName = groupName;
            pythonCmd = rootFolder + pythonPath;
        }

        public void GenerateAll()
        {
            int p1 = ordinal;
            run(p1.ToString(), "0", "0", "0");
            for (int p2 = 1; p2 <= ordinal; p2++)
            {
                for (int p3 = p2 + 1; p3 <= ordinal; p3++)
                {
                    int p4 = 1;
                    run(p1.ToString(), p2.ToString(), p3.ToString(), p4.ToString());
                    p4 = 2;
                    run(p1.ToString(), p2.ToString(), p3.ToString(), p4.ToString());
                }
            }
        }

        private void run(string arg1, string arg2, string arg3, string arg4) 
        {
            run_cmd(arg1, arg2, arg3, arg4);
            String outputFileName = groupName + "_" + arg2 + "_" + arg3 + "_" + arg4 + ".png";

            string binDirectory = rootFolder + binPath;
            string outputDirectory = rootFolder + outputPath;
            if (Directory.Exists(binDirectory))
            {
                string[] fileEntries = Directory.GetFiles(binDirectory);
                foreach(string fileName in fileEntries)
                    File.Copy(fileName, outputDirectory + outputFileName, true);
                Console.WriteLine("Copied a file to " + outputDirectory + outputFileName);
            }
            else 
            {
                Console.WriteLine("Bin directory does not exist: " + binDirectory);
            }
        }

        private void run_cmd(string arg1, string arg2, string arg3, string arg4)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = @"X:\XXXXXXXXXXXXXXXXX\Programs\Python\Python311\python.exe";
            start.Arguments = string.Format("{0} {1} {2} {3} {4}", pythonCmd, arg1, arg2, arg3, arg4);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using(Process process = Process.Start(start))
            {
                using(StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    Console.Write(result);
                }
            }
        }
    }
}
