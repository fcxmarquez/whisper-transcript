import { useState } from 'react'
import { Box, VStack, Heading, Button, Text, Textarea } from '@chakra-ui/react'

export const Home = () => {
  const [file, setFile] = useState<File | null>(null)
  const [transcription, setTranscription] = useState('')

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0])
    }
  }

  const handleTranscribe = () => {
    // Implement transcription logic here
    setTranscription('This is the transcribed text.')
  }

  return (
    <>
      <Box minHeight="100vh" bg="gray.900" color="white" p={8} display="flex" flexDirection="column" justifyContent="space-between">
        <Box display="flex" justifyContent="center" alignItems="center" flex="1">
          <VStack spacing={6} maxWidth="400px">
            <Heading>Whisper Transcript</Heading>
            <Box width="100%">
              <input
                type="file"
                accept="audio/*"
                onChange={handleFileChange}
                style={{ display: 'none' }}
                id="file-input"
              />
              <label htmlFor="file-input">
                <Button as="span" colorScheme="blue" width="100%">
                  Choose File
                </Button>
              </label>
              <Text mt={2} fontSize="sm">
                {file ? file.name : 'No file chosen'}
              </Text>
            </Box>
            <Button
              colorScheme="blue"
              width="100%"
              onClick={handleTranscribe}
              isDisabled={!file}
            >
              Upload & Transcribe
            </Button>
            <VStack width="100%" align="start">
              <Text fontWeight="bold">Transcription:</Text>
              <Textarea
                value={transcription}
                readOnly
                bg="gray.700"
                borderColor="gray.600"
                height="100px"
              />
            </VStack>
          </VStack>
        </Box>
        <Text textAlign="center" fontSize="sm" mt={4}>
          Made by <Text as="span" fontWeight="bold">fcxmarquez</Text>
        </Text>
      </Box>
    </>
  )
}